
<?php 

date_default_timezone_set('UTC');

	
if(isset($_REQUEST['add_student']))	
{
	$student_number = $_REQUEST['student_number'];
	$name = $_REQUEST['name'];
	$address = $_REQUEST['address'];
	$gender = $_REQUEST['gender'];
	$course_code = $_REQUEST['course_code'];
	$course_name = $_REQUEST['course_name'];
	$degree_type = $_REQUEST['degree_type'];
	$room_number = $_REQUEST['room_number'];
	$violations = $_REQUEST['violations'];
	$violation_date = $_REQUEST['violation_date'];
	$eviction = $_REQUEST['eviction'];
	$move_in_date = $_REQUEST['move_in_date'];
	$room_service_order = $_REQUEST['room_service_order'];
	$room_inspection = $_REQUEST['room_inspection'];
	$bill = $_REQUEST['bill'];
	
	mysql_connect('localhost', 'root', '');
	if (mysqli_connect_errno())
	{
		echo "Failed to connect to MySQL: " . mysqli_connect_error();
	}
	mysql_select_db('student_residence');

			
	$sql = "INSERT INTO `Student`(`student_number`, `name`, `address`, `gender`,
	 `course_name`, `course_code`, `degree_type`, `room_number`, `move_in_date`, 
	 `violations`, `violation_date`, `room_inspection`, `room_service_order`, `eviction`, `bill`)
	  VALUES ('%s','%s','%s','%s','%s','%s','%s','%d','%s','%d','%s','%s','%s','%s','%d')";
	  $sql = sprintf("$sql",$student_number, $name, $address, $gender, $course_name, $course_code, $degree_type, $room_number,$move_in_date,$violations,$violation_date,$room_inspection, $room_service_order, $eviction, $bill);
	
	//print "".$sql."";
	$result = mysql_query($sql);


	
}
	?>


<html>

<head>
<link rel="stylesheet" type ="text/css" href="stylesheet.css"  >

</head>

<body>

<!--This is the header-->
<table class = "banner_menu" border='0'>

	<tr valign="top">
		<td width="12%"></td>
		<td width="76%" height = "14%" colspan='1'>
			<a href="home.html"><img src = "images/dit_crest_2010.gif"></a>
			<a href="home.html"><img src = "images/dit_logo_text.png"></a>
		</td>
		<td width="12%"></td>
	</tr>
</table>

<table class="banner_menu" border="0">
	<tr>
		<td width="12%"></td>
		<td class ="the_little_four" >
			<div onclick="location.href='home.php'" style= "cursor:pointer;width:100%; height:100%;">
				
					<font class="button_font">Home</font>
				
			</div>
		</td>
		<td class ="the_little_four" >
			<div onclick="location.href='records.php'" style= "cursor:pointer;width:100%; height:100%;">
				
					<font class="button_font">Records</font>
				
			</div>
		</td>
		<td class ="the_little_four" >
			<div onclick="location.href='billing.php'" style= "cursor:pointer;width:100%; height:100%; ">
				
					<font class="button_font">Members</font>
				
			</div>
		</td>

		<td class ="current_page" >
			<div onclick="location.href='room_service.php'" style= "cursor:pointer;width:100%; height:100%; ">
				
					<font class="button_font">Edit</font>
				
			</div>
		</td>
		<td width="12%"></td>
	</tr>
</table>


<!--This is the end of the header-->
<!--This is the records module-->

<table width="100%" height="66%" border="0" style="vertical-align: top;">
<tr style="vertical-align: top;">
	<td width="12%"></td>
	<td width="76%">
	
	
	<table class="calendar_title_row" border="0" width = "100%" >
	<tr>
	
			<td class ="current_page_mini" >
			<div onclick="location.href='add.php'" style= "cursor:pointer;width:100%; height:100%; ">
				
					<font class="button_font">Add Student</font>
				
			</div>
		</td>
	
			<td class ="the_little_three" >
			<div onclick="location.href='edit.php'" style= "cursor:pointer;width:100%; height:100%; ">
				
					<font class="button_font">Edit Student</font>
				
			</div>
		</td>
			
			<td class ="the_little_three" >
			<div onclick="location.href='delete.php'" style= "cursor:pointer;width:100%; height:100%; ">
				
					<font class="button_font">Delete Student</font>
				
			</div>
		</td>
	</tr>
	</table>
	<form>
		<table class="calendar_title_row" border="1" >
			<form action='add.php' method='GET'>
			<tr height="100%">
				<td width="35.2%">Student Number: <input class = 'add_field' type="text" name="student_number"></td>

				<td width="35.7%">Name: <input class = 'add_field' type="text" name="name"></td>

				<td width="40%">Address: <input class = 'add_field' type="text" name="address"></td>
			</tr>
			<tr height="100%">
				<td width="33%">Gender: <input class = 'add_field' type="text" name="gender"></td>

				<td width="33%">Course Name: <input class = 'add_field' type="text" name="course_name"></td>

				<td width="33%">Course Code: <input class = 'add_field' type="text" name="course_code"></td>
			</tr>
			<tr height="100%">
				<td width="33%">Degree Type: <input class = 'add_field' type="text" name="degree_type"></td>

				<td width="33%">Room Number: <input class = 'add_field' type="text" name="room_number"></td>

				<td width="33%">Move In Date: <input class = 'add_field' type="text" name="move_in_date"></td>
			</tr>
			<tr height="100%">
				<td width="33%">Violations: <input class = 'add_field' type="text" name="violations"></td>

				<td width="33%">Violation Date: <input class = 'add_field' type="text" name="violation_date"></td>

				<td width="33%">Room Inspection: <input class = 'add_field' type="text" name="room_inspection"></td>
			</tr>
			<tr height="100%">
				<td width="33%">Room Service Order: <input class = 'add_field' type="text" name="room_service_order"></td>

				<td width="33%">Eviction: <input class = 'add_field' type="text" name="evictions"></td>

				<td width="33%">Bill: <input class = 'add_field' type="text" name="bill"></td>
			</tr>
			<tr height="100%">
				<td style="width: 5%; vertical-align: middle;">
				<button type="submit" name='add_student' >Add Student</button>
			</td>
			</tr>
			<form>
	</table>

		


	
<td width="12%"></td>
</tr>
</table>
	


<!-- This is the footer-->

<table class="footer_table" border='0'>
	<tr>
		<td width="12%"></td>
		<td>
		<table class="mini_footer_table">
		<tr>
			<td class="footer"><a style="hover-color:#ffcc33"href="home.html"><font class="button_font">Home</font></a></td>	
			<td class="footer"><font class="button_font">Helpline No: 01 402 3000</font></td>
			<td class="footer"><a href="http://mydit.ie/mydit.ie/"><font class="button_font">Staff Email</font></a></td> 
			<td class="footer"><a href="www.dit.ie"><font class="button_font">DIT Website</font></a></td>
		</tr>
		</table>
		<td>
		<td width="12%"></td>
	</tr>
</table>


</body>

</html>