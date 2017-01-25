#!/bin/bash
sbatch <<EOT
#!/bin/sh
#SBATCH -n 1 -J $1 --cpus-per-task=12 -x node10[01-30],node2015 -e slurm-%j-$1.err -o slurm-%j-$1.out --time=30-00:00:00

/data/junhao/sqmc/runs/run_hci $*
EOT
