#! bin/bash

mu2eg4bl --in=xAngle_0.0mrad.in --tar=Geometry.tar --njobs=20 --events-per-job=50000 --jobname=angleEdge_xAngle_0.0mrad.in --g4bl-version=v2_16a --outstage=/pnfs/mu2e/scratch/outstage;
sleep 1;
mu2eg4bl --in=xAngle_2.618mrad.in --tar=Geometry.tar --njobs=20 --events-per-job=50000 --jobname=angleEdge_xAngle_2.618mrad.in --g4bl-version=v2_16a --outstage=/pnfs/mu2e/scratch/outstage;
sleep 1;
mu2eg4bl --in=xAngle_-2.618mrad.in --tar=Geometry.tar --njobs=20 --events-per-job=50000 --jobname=angleEdge_xAngle_-2.618mrad.in --g4bl-version=v2_16a --outstage=/pnfs/mu2e/scratch/outstage;
sleep 1;
mu2eg4bl --in=xAngle_1.309mrad.in --tar=Geometry.tar --njobs=20 --events-per-job=50000 --jobname=angleEdge_xAngle_1.309mrad.in --g4bl-version=v2_16a --outstage=/pnfs/mu2e/scratch/outstage;
sleep 1;
mu2eg4bl --in=xAngle_-1.309mrad.in --tar=Geometry.tar --njobs=20 --events-per-job=50000 --jobname=angleEdge_xAngle_-1.309mrad.in --g4bl-version=v2_16a --outstage=/pnfs/mu2e/scratch/outstage;
sleep 1;
mu2eg4bl --in=xAngle_0.6545mrad.in --tar=Geometry.tar --njobs=20 --events-per-job=50000 --jobname=angleEdge_xAngle_0.6545mrad.in --g4bl-version=v2_16a --outstage=/pnfs/mu2e/scratch/outstage;
sleep 1;
mu2eg4bl --in=xAngle_-0.6545mrad.in --tar=Geometry.tar --njobs=20 --events-per-job=50000 --jobname=angleEdge_xAngle_-0.6545mrad.in --g4bl-version=v2_16a --outstage=/pnfs/mu2e/scratch/outstage;
sleep 1;
mu2eg4bl --in=xAngle_1.964mrad.in --tar=Geometry.tar --njobs=20 --events-per-job=50000 --jobname=angleEdge_xAngle_1.964mrad.in --g4bl-version=v2_16a --outstage=/pnfs/mu2e/scratch/outstage;
sleep 1;
mu2eg4bl --in=xAngle_-1.964mrad.in --tar=Geometry.tar --njobs=20 --events-per-job=50000 --jobname=angleEdge_xAngle_-1.964mrad.in --g4bl-version=v2_16a --outstage=/pnfs/mu2e/scratch/outstage;
sleep 1;
