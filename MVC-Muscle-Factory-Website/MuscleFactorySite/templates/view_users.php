<?php

include_once './db/simple_db_manager.php';

echo "<div style='text-align:center; color:black;'><h2>Account Information </h2></div>";
echo "<div style='overflow:auto;height:400px'>";
echo "<table class= 'table table-hover ' border='1' style='width:100%; text-align:left; background-color:grey; color:black; margin:0px'>";
echo "<thead style='background-color:#c3a896'>";
echo "<tr>
<th>ID  </th>
<th>Username:   </th>
<th>Email:   </th>
<th>Full name:   </th>
</tr>";

echo "</thead>";
foreach ($this->model->allUsers as $row){
	echo "<td>" . $row ['user_id'] . "</td>";
	echo "<td>" . $row ['user_name'] . "</td>";
    echo "<td>" . $row ['email'] . "</td>";
	echo "<td>" . $row ['full_name'] . "</td>";
	echo "</tr>";
}
echo "</table>";
echo "</div>";
?>

<html>
<head>
<link href ="css/misc.css" rel="stylesheet" type="text/css">
</head>
</html>