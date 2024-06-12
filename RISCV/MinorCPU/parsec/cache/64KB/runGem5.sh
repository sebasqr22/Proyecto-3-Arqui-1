# -- an example to run SPEC 429.mcf on gem5, put it under 429.mcf folder --
export GEM5_DIR=/home/mario/Documents/GEM5/gem5
export BENCHMARK=./src/blackscholes
export INPUT=./in_16.txt
export OUTPUT=./output.txt
export NTHREADS=1
time $GEM5_DIR/build/RISCV/gem5.opt -d m5out/ $GEM5_DIR/configs/deprecated/example/test.py -c $BENCHMARK -o "$NTHREADS $INPUT $OUTPUT" -I 1000000000 --cpu-type=MinorCPU --caches --l2cache --l1d_size=64kB -I 10000000 --cpu-type=MinorCPU --caches --l2cache --l1d_size=64kB --l1i_size=64kB --l2_size=1MB --l1d_assoc=2 --l1i_assoc=2 --l2_assoc=1 --cacheline_size=64 --bp-type=BiModeBP --replacement_policy=lru
