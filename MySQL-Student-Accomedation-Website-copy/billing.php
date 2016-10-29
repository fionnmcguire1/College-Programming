<?php

include("security.php");

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
		<td class ="current_page" >
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
<table width="100%">
<?php
			print "<tr style='vertical-align: top; text-align: center;'>";
			print "<td width= '12%'>";
			
				print "<td class='records_list'>Member Type</td>";
			
				print "<td class='records_list'>Username</td>";
		
				print "<td class='records_list'>Full Member Name</td>";
			print "<td width= '12%'>";
			print "</tr>";

			print "<tr style='vertical-align: top; text-align: center;'>";
			print "<td width= '12%'>";
			

			print "</tr>";
	mysql_connect('localhost', 'root', '');
	if (mysqli_connect_errno())
	{
		echo "Failed to connect to MySQL: " . mysqli_connect_error();
	}
	mysql_select_db('student_residence');

			
	$sql = "SELECT * from members";
	$result = mysql_query($sql);

	if ($result > 0) 
	{
	
		while($Student=mysql_fetch_assoc($result))
		{
			if($Student['admin'] == 1)
			{
				$administrator = "Administrator";
			}
			else
			{
				$administrator = "Regular";
			}
	
			print "<tr style='vertical-align: top; text-align: center;'>";
			print "<td width= '12%'>";
			
				print "<td class='records_list'>$administrator</td>";
			
				print "<td class='records_list'>".$Student['username']."</td>";
			
				
			
				print "<td class='records_list'>".$Student['name']."</td>";
			print "<td width= '12%'>";
			print "</tr>";
		

		} 
	}

?>
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