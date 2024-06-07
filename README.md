# GFDL Notebooks
(Previously MAR - Model Analysis Repository)

<p>
The Latin word <i>"mar"</i> translates to <i>"sea"</i>. This repository will contain a collection of (mainly) ocean-focused analyses to 
  inform next-generation ocean and climate model development.
</p>

## Ways to Run MAR

1. Interactively (clone the repository, edit the notebooks, and run)
2. Execute the batch script `run_mar.sh`
3. Visit https://dora.gfdl.noaa.gov/analysis/mar

## Contributing to MAR
Jupyter notebooks are the encapsulation of a particular analysis.  There are relatively few constraints on how an analysis built, but there are 
a few interfaces to be aware of:

### Configuration / Environment Variables
The batch and web engines for MAR (items 2 and 3 above) will set two runtime environment variables. Use one or both of these fields to 
determine the top-level path to a model experiment to analyze:

* `MAR_DORA_ID`: The experiment ID in the dora database
* `MAR_PATHPP`: The top-level path to the post-processing experiment directory of the experiment (e.g. `/some/path/pp/`)

Each notebook should have a default set of model years to analyze (e.g. 1981-2010).  The MAR engines will also provide two optional, additional variables, 
`STARTYR` and `ENDYR`, that can be used to override the defaults in the notebook.

### Scalar Results / Metrics

If your notebook produces scalar metrics, it should write those results to a YAML file.  See the `SST_bias_NOAA_OISSTv2.ipynb` notebook for an example of 
how to construct a YAML file. Some examples of scalar fields might be RMSE and bias of a field, or the average depth of the Mediterranean outflow plume.


