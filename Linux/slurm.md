canceling all jobs

    scancel -u <username>

check running jobs

    squeue -u <username>

check heistory 

    sacct --starttime 2024-07-01 --endtime 2024-08-01
    sacct --starttime 2024-12-01 --format=JobName%10,CPUTime%10,Elapsed%10,State%10,JobID%10 -X

SBATCH settings

#SBATCH --time=DD-HH:MM:SS

