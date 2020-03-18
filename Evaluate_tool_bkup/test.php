<?php
$start  = "2016-06-01";
$end    = "2016-06-02";
$command="py -3 D:\bokai\python\python-code\Evaluate_tool\Meteorology.py" .' '. $start.' '. $end ;
print_r($command);
// print_r()
exec($command);


?>