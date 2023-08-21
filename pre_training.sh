#!/bin/sh
export PYTHONUNBUFFERED=1
export DATA_DIR=/data/run01/scv2382/yfliu/sywang/5mc_bert5/else_data/dataset/
export BERT_BASE_DIR=/data/run01/scv2382/yfliu/sywang/5mc_bert5/;
python2 run_pretraining.py --input_file=$DATA_DIR/pre/5mc-1/hg3_data.tfrecord --output_dir=BERT_BASE_DIR/pre_train/5mc-1/ --do_train=True --do_eval=True --bert_config_file=BERT_BASE_DIR/bert_config_1.json --train_batch_size=32 --max_seq_length=256 --max_predictions_per_seq=20 --num_train_steps=200000 --num_warmup_steps=10000 --learning_rate=5e-5
