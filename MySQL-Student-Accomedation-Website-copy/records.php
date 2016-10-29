
<?php 

date_default_timezone_set('UTC');

$SN = 0;
$N = 0;
$A = 0;
$G = 0;
$CN = 0;
$DT = 0;
$CC = 0;
$RN = 0;
$RT = 0;
$MID = 0;
$V = 0;

		
		

if(isset($_REQUEST['update_view']))
{

	$no_of_selected_items = 0;
	


	
	$RI = 0;
	if(isset($_REQUEST['student_no']) && $no_of_selected_items < 6)
	{
		$SN = 1;
		$no_of_selected_items = $no_of_selected_items+1;
		/*
		$remove_task_id=$_REQUEST['task_id'];
		$remove_member_task_id=$_REQUEST['member_task_id'];
		$Query=sprintf("$remove_task",$remove_task_id,$remove_member_task_id,$remove_task_id);
		$DBConnection->Exec($Query);
		*/
	}

	$N = 0;
	if(isset($_REQUEST['name']) && $no_of_selected_items < 6)
	{
		$N = 1;
		$no_of_selected_items = $no_of_selected_items+1;
		

	}

	$A = 0;
	if(isset($_REQUEST['address']) && $no_of_selected_items < 6)
	{
		$A = 1;
		$no_of_selected_items = $no_of_selected_items+1;

	}


	$G = 0;
	if(isset($_REQUEST['gender']) && $no_of_selected_items < 6)
	{
		$G = 1;
		$no_of_selected_items = $no_of_selected_items+1;

	}
	$CN = 0;
	if(isset($_REQUEST['course_name']) && $no_of_selected_items < 6)
	{
		$CN = 1;
		$no_of_selected_items = $no_of_selected_items+1;

	}
	$CC = 0;
	if(isset($_REQUEST['course_code']) && $no_of_selected_items < 6)
	{
		$CC = 1;
		$no_of_selected_items = $no_of_selected_items+1;

	}
	$DT = 0;
	if(isset($_REQUEST['degree_type']) && $no_of_selected_items < 6)
	{
		$DT = 1;
		$no_of_selected_items = $no_of_selected_items+1;

	}
	$RN = 0;
	if(isset($_REQUEST['room_number']) && $no_of_selected_items < 6)
	{
		$RN = 1;
		$no_of_selected_items = $no_of_selected_items+1;

	}
	$RT = 0;
	if(isset($_REQUEST['room_type']) && $no_of_selected_items < 6)
	{
		$RT = 1;
		$no_of_selected_items = $no_of_selected_items+1;

	}
	$MID = 0;
	if(isset($_REQUEST['moved_in_date']) && $no_of_selected_items < 6)
	{
		$MID = 1;
		$no_of_selected_items = $no_of_selected_items+1;

	}
	$V = 0;
	if(isset($_REQUEST['violations']) && $no_of_selected_items < 6)
	{
		$V = 1;
		$no_of_selected_items = $no_of_selected_items+1;

	}


}

if($SN == 0 && $N == 0 && $A == 0 && $G == 0 && $CN == 0 && $DT == 0 && $CC == 0 && $RN == 0 && $RT == 0 && $MID == 0 && $V == 0)
{
	$SN = 1;
	$N = 1;
	$A = 1;
	$G = 1;
	$CN = 1;
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
		<td class ="current_page" >
			<div onclick="location.href='records.php'" style= "cursor:pointer;width:100%; height:100%;">
				
					<font class="button_font">Records</font>
				
			</div>
		</td>
		<td class ="the_little_four" >
			<div onclick="location.href='billing.php'" style= "cursor:pointer;width:100%; height:100%; ">
				
					<font class="button_font">Members</font>
				
			</div>
		</td>

		<td class ="the_little_four" >
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
	<form action = "records.php" method="GET">
		<table class="calendar_title_row" border="0" >

			<tr height="100%">
			<td class="calendar_title">
				<?php
				if($SN == 1)
				{
					print "Student number  <input type='checkbox' name='student_no' value='student_no' checked><br>";
				}
				if($SN == 0)
				{
					print "Student number  <input type='checkbox' name='student_no' value='student_no' ><br>";
				}
				if($N == 1)
				{
					print "Name  <input type='checkbox' name='name' value='name' checked><br>";
				}
				if($N == 0)
				{
					print "Name  <input type='checkbox' name='name' value='name' ><br>";
				}
				if($A == 1)
				{
					print "Address  <input type='checkbox' name='address' value='address' checked><br>";
				}
				if($A == 0)
				{
					print "Address  <input type='checkbox' name='address' value='address' ><br>";
				}
				
				
				?>
			</td>
			<td class="calendar_title">
				<?php
				if($G == 1)
				{
					print "Gender  <input type='checkbox' name='gender' value='gender' checked><br>";
				}
				if($G == 0)
				{
					print "Gender  <input type='checkbox' name='gender' value='gender' ><br>";
				}
				if($CN == 1)
				{
					print "Course Name  <input type='checkbox' name='course_name' value='course_name' checked><br>";
				}
				if($CN == 0)
				{
					print "Course name  <input type='checkbox' name='course_name' value='course_name' ><br>";
				}
				if($CC == 1)
				{
					print "Course code  <input type='checkbox' name='course_code' value='course_code' checked><br>";
				}
				if($CC == 0)
				{
					print "Course code  <input type='checkbox' name='course_code' value='course_code' ><br>";
				}
				
				
				?>
			</td>
			<td class="calendar_title">
				<?php
				if($DT == 1)
				{
					print "Degree type  <input type='checkbox' name='degree_type' value='degree_type' checked><br>";
				}
				if($DT == 0)
				{
					print "Degree type  <input type='checkbox' name='degree_type' value='degree_type' ><br>";
				}
				if($RN== 1)
				{
					print "Room number  <input type='checkbox' name='room_number' value='room_number' checked><br>";
				}
				if($RN == 0)
				{
					print "Room number  <input type='checkbox' name='room_number' value='room_number' ><br>";
				}
				if($RT == 1)
				{
					print "Bill  <input type='checkbox' name='room_type' value='room_type' checked><br>";
				}
				if($RT == 0)
				{
					print "Bill  <input type='checkbox' name='room_type' value='room_type' ><br>";
				}
				
				
				?>
			</td>
			<td class="calendar_title" style="vertical-align: top;">
				<?php
				if($MID == 1)
				{
					print "Moved in  <input type='checkbox' name='moved_in_date' value='move_in_date' checked><br>";
				}
				if($MID == 0)
				{
					print "Moved in  <input type='checkbox' name='moved_in_date' value='moved_in_date' ><br>";
				}
				if($V == 1)
				{
					print "Violations  <input type='checkbox' name='violations' value='violations' checked><br>";
				}
				if($V == 0)
				{
					print "Violations  <input type='checkbox' name='violations' value='violations' ><br>";
				}
				
				
				?>
			</td>
						<td style="width: 5%; vertical-align: middle;">
				<button type="submit" name='update_view' >Update</button>
			</td>
			</form>
		</tr>

	</table>
<table width="100%">
	<tr style="vertical-align: top; text-align: center;">
	<?php
	if($SN == 1)
		print "<td class='records_list'>Student No</td>";
	if($N == 1)
		print "<td class='records_list'>Name";
		print"</td>";
	if($A == 1)
		print "<td class='records_list'>Address</td>";
	if($G == 1)
		print "<td class='records_list'>Gender</td>";
	if($CN == 1)
		print "<td class='records_list'>Course Name</td>";
	if($DT == 1)
		print "<td class='records_list'>Degree Type</td>";
	if($CC == 1)
		print "<td class='records_list'>Course Code</td>";
	if($RN == 1)
		print "<td class='records_list'>Room No</td>";
	if($RT == 1)
		print "<td class='records_list'>Bill</td>";
	if($MID == 1)
		print "<td class='records_list'>Moved In</td>";
	if($V == 1)
		print "<td class='records_list'>Violations</td>";
	?>



	
	<?php
	
	
	mysql_connect('localhost', 'root', '');
	if (mysqli_connect_errno())
	{
		echo "Failed to connect to MySQL: " . mysqli_connect_error();
	}
	mysql_select_db('student_residence');

			
	$sql = "SELECT * from Student";
	$result = mysql_query($sql);

	if ($result > 0) 
	{

		while($Student=mysql_fetch_assoc($result))
		{
	
			print "<tr style='vertical-align: top; text-align: center;'>";
			if($SN == 1)
				print "<td class='records_list'>".$Student['student_number']."</td>";
			if($N == 1)
				print "<td class='records_list'>".$Student['name']."</td>";
			if($A == 1)
				print "<td class='records_list'>".$Student['address']."</td>";
			if($G == 1)
				print "<td class='records_list'>".$Student['gender']."</td>";
			if($CN == 1)
				print "<td class='records_list'>".$Student['course_name']."</td>";
			if($DT == 1)
				print "<td class='records_list'>".$Student['degree_type']."</td>";
			if($CC == 1)
				print "<td class='records_list'>".$Student['course_code']."</td>";
			if($RN == 1)
				print "<td class='records_list'>".$Student['room_number']."</td>";
			if($RT == 1)
				print "<td class='records_list'>¢".$Student['bill']."</td>";
			if($MID == 1)
				print "<td class='records_list'>".$Student['move_in_date']."</td>";
			if($V == 1)
				print "<td class='records_list'>".$Student['violations']."</td>";
			print "</tr>";
		

		} 
	}
	else 
	{
		echo "0 results";
	}
	
	
	
	
	
	/*
	$j = 0;
	while($j < 50)
	{

	$j = $j+1;
	}*/
	?>
		
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