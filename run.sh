mkdir predictions_50000
cat datasets/filelist/val.txt | while read line
do
  echo $line
  #echo "predictions_"${line##*/}
  ./darknet detector test cfg/in_car.data cfg/yolov3-in_car.cfg ./datasets/backup/yolov3-in_car_50000.weights $line
  mv predictions.png "./predictions_50000/predictions_"${line##*/}
done
