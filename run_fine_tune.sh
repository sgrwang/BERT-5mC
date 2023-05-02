#!/bin/sh
export DATA_DIR=/mnt/raid5/data2/sywang/5mc/else_data/6mA/tt/;
export BERT_BASE_DIR=/mnt/raid5/data2/sywang/5mc;
python my_run_classifier.py --task_name=mytask --do_train=true --do_eval=false --do_predict=true --do_lower_case=True --data_dir=$DATA_DIR/ --vocab_file=$BERT_BASE_DIR/pre/5mc-3/vocab_3kmer.txt --bert_config_file=$BERT_BASE_DIR/pre/5mc-3/bert_config_3.json --init_checkpoint=$BERT_BASE_DIR/pre/5mc-3/model.ckpt-200000 --max_seq_length=256 --train_batch_size=32 --learning_rate=2e-5  --num_train_epochs=4.0 --output_dir=/mnt/raid5/data2/sywang/5mc/fine_tune/else/6ma/tt/;



