#!/bin/sh
export PYTHONUNBUFFERED=1
export DATA_DIR=/data/run01/scv2382/yfliu/sywang/5mc_bert5/else_data/dataset/
export BERT_BASE_DIR=/data/run01/scv2382/yfliu/sywang/5mc_bert5/;
python2 create_pretraining_data.py --input_file=$DATA_DIR/pre/hg3_data.txt --output_file=$DATA_DIR/pre/hg3_data.tfrecord --vocab_file=$BERT_BASE_DIR/vocab_5kmer.txt --do_lower_case=True --max_seq_length=256 --max_predictions_per_seq=20 --masked_lm_prob=0.15 --random_seed=12345 --dupe_factor=5
