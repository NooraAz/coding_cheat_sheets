canceling all jobs

    scancel -u <username>

check running jobs

    squeue -u <username>

check heistory 

    sacct --starttime 2024-07-01 --endtime 2024-08-01
    sacct --starttime 2024-12-01 --format=JobName%10,CPUTime%10,Elapsed%10,State%10,JobID%10 -X

SBATCH settings

    #SBATCH --time=DD-HH:MM:SS

**Flatiron partitions:**

|Partition|	Notes|#Cores/nodes limit|Time limit|Exclusive?|Flags|
|---------|------|------------------|----------|----------|-----|
|General          |Default partition| 4 nodes or 256 cores|	1 week (default: 1 day)|	Yes|	-p gen|
|Express Serial   |	For small serial jobs|	256 cores|	1 week (default: 6 hours)|	No	|-p genx|
|Center partitions|For regular large jobs|	2560 cores/user and 45 nodes/user|	1 week	|Yes	|-p cc<X>|
|Big Memory	Single-node |big memory jobs (3-6TB)	|2 nodes	|1 week|Yes|	-p mem|
|Preemptive	|For large jobs with checkpoint/restart	|No limit|	1 week |Yes	|-p preempt --qos=preempt|
|Request	|For large jobs running during off-hours|	-	|1 week	|Yes|-p request --qos=request|
|GPU	    |For GPU nodes	|32 GPUs (popeye: 40 GPUs)|1 week|No|-p gpu|
|GPU Preempt|For preemptable GPU jobs|	No limit	|1 week|No|-p gpupreempt -q gpupreempt|
|GPU XL	    |For large parallel GPU jobs|	12 nodes (48 GPUs)	|2 days	|Yes	|-p gpuxl|
|Legacy GPU |For legacy GPU nodes|	-	|1 week	|No	|-p legacygpu|



Talapas partitions:


