#!/usr/bin/env bash

experiment=$1
outdir=$2
rootdir=`pwd`
kernel_name="python3"

echo $experiment

if [[ -z "$outdir" ]]; then
    outdir="."
fi

outdir="${outdir}/${experiment}"

echo "MAR: writing results to ${outdir}"

export PYDEVD_DISABLE_FILE_VALIDATION=1
export MAR_DORA_ID=$experiment

env | grep "MAR"

mkdir -p $outdir

pushd $outdir
pwd
for notebook in ${rootdir}/*.ipynb; do
   filename=`basename $notebook`
   echo "Executing ${filename}"
   cp ${notebook} .
   jupyter nbconvert --to notebook --execute --ExecutePreprocessor.kernel_name=$kernel_name "$filename" --output "${filename}"
   jupyter nbconvert --to html "${filename}"
done

popd

exit
