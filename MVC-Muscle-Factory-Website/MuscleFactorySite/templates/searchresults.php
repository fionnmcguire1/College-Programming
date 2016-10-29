<?php

include_once 'templates/html_doctype_and_head.php'; 
include_once 'search_form.php';

echo "<h3 style='color:white' > Search Results :<br></h3><h2 style='color:cyan'></h2>";
echo "<div style='overflow:auto;height:200px;'>";
echo "<table class='table table-striped border='1' style='width:100%; text-align:left; background-color:grey; color:black; margin:0px'>";
echo "<thead style='background-color:#c3a896'>";
echo "<tr>
<th>ID  </th>
<th>Name:   </th>
<th>Description:   </th>
<th>Type:   </th>
</tr>";
echo "</thead>";


foreach ($this->model->searchResults as $row){
	echo "<td>" . $row ['ex_id'] . "</td>";
	echo "<td>" . $row ['ex_name'] . "</td>";
	echo "<td>" . $row ['ex_desc'] . "</td>";
	echo "<td>" . $row ['type'] . "</td>";
	echo "</tr>";
}

echo "</table>";
echo "</div>";

echo "<form action='index.php' method='post'>";
	echo "<button type='submit' class='btn btn-success'> Go Back </button>";
echo "</form>";





?>

<html>
<head>

<link href ="css/misc.css" rel="stylesheet" type="text/css">

</head>
</html>