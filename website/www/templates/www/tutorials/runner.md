
#The ExperimentRunner: Experiment replication
Network measurements present variability due to the underlying stochastic processes that affect the outcome of the measured phenomena (e.g. network delay, packet loss, etc). To obtain results that are statistically representative of the phenomena under study a same experiment can be re-executed many times in order to collect many data samples. The obtained data can then be analyzed using a statistical method.

###The ExperimentRunner
The ExperimentRunner is intended to automate re-execution of a same experiment until a criteria defined by the experimenter is satisfied. The example below shows the use of an ExperimentRunner.

<pre><code class="python">from nepi.execution.runner import ExperimentRunner

rnr = ExperimentRunner()
runs = rnr.run(ec, min_runs = 10, max_runs = 300,
       compute_metric_callback = avg_interests,
       evaluate_convergence_callback = normal_convergence,
       wait_guids = resources,
       wait_time = 0)
</code></pre>

The ExperimentRunner constructor takes the following arguments:

- -**ec**: ExperimentController instance with the experiment description
- -**min_runs**: minimum number of times to run the experiment
- -**max_runs**: maximum number of times to run the experiment
- -**compute\_metric\_callback**: function to compute the metric of insterest after each experiment run
- -**evaluate\_convergence\_callback**: optional function to evaluate if the metric converged according to a criteria defined by the experimenter
- -**wait\_guids**: list of resources to wait to be finished before ending each run
- -**wait\_time**: (alternative to wait_guids) time to wait in seconds between the experiment deployment and the experiment release on each run

###compute\_metric\_callback
The compute_metric_callback is a user defined function invoked after each experiment run in order to compute a metric. It can us traces collected during experiment execution. The function receives as arguments the ec and the current run number. It must return a single value with the computed metric (usually a single numerical value, but it it can also be an array or dictionary).

<pre><code class="python">metric = compute_metric_callback(ec, run)
</code></pre>

The result of the function is added to a samples list. The list of samples with all previously computed metrics is given as argument to the evaluate_converged_callback function after each run. This function determines using the list of sample if the experiment should be run again or not.

###evaluate\_convergence\_callback
The evaluate_convergence_callback function decides whether enough measurements have been collected, given the history of computed metrics. This function receives as arguments the ExperimentController, the current run number, and the list of samples. The list of samples stores the result given by the compute_metric_callback for run "i" at position "i" (i.e. metrics[0] holds the metrics computed by compute_metric_callback for run 0)

<pre><code class="python">stop = evaluate_convergence_callback(ec, run, metrics)
</code></pre>

This function must return False if the experiment should be run again, and True if no more runs should be made. The default implementation of the evaluate_convergence_callback function is given below:

<pre><code class="python">def evaluate_normal_convergence(ec, run, metrics):
   # sample
   x = numpy.array(metrics)
   # number of elements in the sample
   n = len(metrics)
   # mean of the sample
   m = x.mean()
   # standard deviation of the sample
   std = x.std()
   # standard error: standard deviation of the sample mean
   se = std / math.sqrt(n)

   # confidence interval with 95% confidence level ~ se * 2 (asuming normal distribution of the sample)
   ci95 = se * 2

   # Converged if the standard error is less than 5% of the mean value
   return m * 0.05 >= ci95
</code></pre>

The evaluate_normal_convergence function assumes that the sample values are normally distributed and terminates the runs when the satndard error is less or equal than 5% of that mean value with a confidence level of 95%.

###!ExperimentRunner execution flow
The figure below shows the steps in the execution flow used by the ExperimentRunner.

![minipicformat](http://nepi.inria.fr/pub/Nepi/ExperimentRunnerTutorial/experiment_runner.png)

###An ExperimentRunner example
The following example uses the LInux ping application to send ICMP requests to the "nepi.inria.fr" host from the localhost machine. The ExperimentRunner is used to re-run the experiment until the round trip time measured by the ping application converges to a mean value with a small standard error, as defined by the default evaluate_convergence_callback function . The experiment is run a minimum of 5 times and a maximum of 300 times.

**Note that ec.deploy should not be invoked, because this is done by the ExperimentRunner, and that only one ExperimentRunner is needed**.


<pre><code class="python">from nepi.execution.ec import ExperimentController
from nepi.execution.runner import ExperimentRunner

ec = ExperimentController(exp_id="runner")

node = ec.register_resource("linux::Node")
ec.set(node, "hostname", "localhost")

app = ec.register_resource("linux::Application")
ec.set(app, "command", "ping -c 5 nepi.inria.fr")
ec.register_connection(app, node)

def min_rtt(ec, run):
   # retrieve the ping application from the ec
   ping = ec.filter_resources("linux::Application")[0]

   # get the ping output
   out = ec.trace(ping, "stdout")

   # find the minimum rtt value from the ping output
   expr = "min/avg/max/mdev = "
   min_rtt = out[out.find(expr) + len(expr): ].strip().split("/")[0]

   # return a numerical value for the minimum rtt
   return float(min_rtt)

rnr = ExperimentRunner()

runs = rnr.run(ec, min_runs=5, max_runs=300,
      compute_metric_callback=min_rtt,
      wait_guids=[app])
</code></pre>
