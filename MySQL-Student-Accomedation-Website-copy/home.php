<html>

<head>
<link rel="stylesheet" type ="text/css" href="stylesheet.css"  >

</head>

<body>

<?php
			$successful_login = "
			<td width='23%' height='14%' valign='middle' align='right'>
			<form style='font-family:arial; color:#0063b1;'action='home.php' method='GET'>
  				Username: <input style='width:40%; color:#ACA7A7;' type='text' name='username' value='example@mydit.ie'><br>
  				Password: <input style='width:40%;'type='password' name='password' value=''><br>
  				<input style='background-color:#0096d7; border-color:#0096D7; text-align:right; color:white' type='submit' name='login' value='Log On'>
			</form>
		</td> ";
	$top_message = "";
	$uname = "";
	$pass = "";

if(isset($_REQUEST['login']))
{
	$uname = $_REQUEST['username'];
	$pass = $_REQUEST['password'];
	
	//print "$uname $pass";
	
	mysql_connect('localhost', 'root', '');
	if (mysqli_connect_errno())
	{
		echo "Failed to connect to MySQL: " . mysqli_connect_error();
	}
	mysql_select_db('student_residence');

			
	$sql = "SELECT * from members where username = '%s' AND password = '%s'";
	$sql = sprintf("$sql", $uname, $pass);
	$result = mysql_query($sql);

	if ($result > 0) 
	{
	
		while($Student=mysql_fetch_assoc($result))
		{
			$successful_login = "
			<td width='23%' height='14%' valign='middle' align='center' style = 'font-size: 300%'>
			Successful login
		</td> ";
		session_start();
		$_SESSION['valid'] = "true";
		
		$top_message = $Student['name'];
		}
	}
	else 
	{
			$successful_login = "
			<td width='23%' height='14%' valign='middle' align='right'>
			<form style='font-family:arial; color:#0063b1;'action='home.php' method='GET'>
  				Username: <input style='width:40%; color:#ACA7A7;' type='text' name='username' value='example@mydit.ie'><br>
  				Password: <input style='width:40%;'type='password' name='password' value=''><br>
  				<input style='background-color:#0096d7; border-color:#0096D7; text-align:right; color:white' type='submit' name='login' value='Log On'>
			</form>
		</td> ";
	}
}
?>

<!--This is the header-->
<table class = "banner_menu" border='0'>

	<tr valign="middle">
		<td width="12%"></td>
		<?php 
		if($top_message == "")
		{
			print "<td width='76%' height = '14%' colspan='1'>
			<a href='home.html'><img src = 'images/dit_crest_2010.gif'></a>
			<a href='home.html'><img src = 'images/dit_logo_text.png'></a>
		</td>";
		}
		else
		{
			print "<td width='56%' height = '14%' colspan='1'>
			<a href='home.html'><img src = 'images/dit_crest_2010.gif'></a>
			<a href='home.html'><img src = 'images/dit_logo_text.png'></a>
			</td>
			<td style = 'width: 20%; font-size: 200%;'>
			$top_message
			</td>";
		}
		?>
		<td width="12%"></td>
	</tr>
</table>

<table class="banner_menu" border="0">
	<tr>
		<td width="12%"></td>
		<td class ="current_page" >
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

		<td class ="the_little_four" >
			<div onclick="location.href='room_service.php'" style= "cursor:pointer;width:100%; height:100%; ">
				
					<font class="button_font">Edit</font>
				
			</div>
		</td>
		<td width="12%"></td>
	</tr>
</table>


<!--This is the end of the header-->


<table class="welcome" border="0">
	<tr height="10%">
	</tr>
	<tr>
		<td width="12%"></td>
		<td width="38%" valign="top">
		<font class="regular_text"><h3>Welcome to the DIT student residence platform</h3></font>
		<p style="color:#ACA7A7;">This facility allows residential staff to adequately monitor all student activity within
		the campus. This platform is a central asset to the DIT porter staff and provides many features at
		your fingertips. Once you log in you will find four buttons above marked Home, Records, Members and Edit
		Records allows you to view all information pertaining to the students, where they're staying
		violations ect. This section allows you to filter this information using various fields.
		For functionality purposes, users may only filter by up to six fields.
		Members holds all information regarding authorised members of this platform. 
		Finally the edit sector of the website allows staff to add, edit or delete records.</p>
		</td>
		<td width="5%"></td>
		<?php print "$successful_login"; ?>
		<td width="10%"></td>
		<td width="12%"></td>
	</tr>
	<tr height="10%">
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

<!--
functionality to login
align text on buttons
get footer to hug the bottom
At the footer hover the font orange
look at getting a nicer font
make input boxes cooler
make buttons cooler
possible search bar
 -->

</body>

</html>
