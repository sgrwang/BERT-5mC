#!/bin/sh
export PYTHONUNBUFFERED=1
export DATA_DIR=/data/run01/scv2382/yfliu/sywang/5mc_bert5/dataset/5mc-3/
export BERT_BASE_DIR=/data/run01/scv2382/yfliu/sywang/5mc_bert5/;
python my_run_classifier.py --task_name=mytask --do_train=false --do_eval=false --do_predict=true --do_lower_case=True --data_dir=$DATA_DIR/ --vocab_file=$BERT_BASE_DIR/vocab_3kmer.txt --bert_config_file=$BERT_BASE_DIR/bert_config_3.json --init_checkpoint=$BERT_BASE_DIR/model/model.ckpt --max_seq_length=256 --train_batch_size=32 --learning_rate=2e-5  --num_train_epochs=4.0 --output_dir=/data/run01/scv2382/yfliu/sywang/5mc_bert5/fine_tune/5mc-3/

