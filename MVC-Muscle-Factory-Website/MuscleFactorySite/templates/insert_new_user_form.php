<h3 style='color:white' > Create New User :<br></h3><h2 style='color:cyan'><legend>Fill in this form to register</legend></h2>
<form action="index.php" method="post">
	<fieldset>
		<input id='action' type='hidden' name='action' value='insertNewUser' />
		<p>
			<label for="Username">Username</label> <input type="text"
				id="Username" name="Username" placeholder="Username"
				maxlength="25" required />
		</p>
		<p>
			<label for="Password">Password</label> <input type="password"
				id="Password" name="Password" placeholder="Password"
				maxlength="25" required />
		</p>
		<p>
			<label for="Email">Email</label> <input type="email"
				id="Email" name="Email" placeholder="Email"
				maxlength="50" required />
		</p>
		<p>
			<label for="fullname">Full Name</label> <input type="text"
				id="fullname" name="fullname" placeholder="Full Name"
				maxlength="50" required />
		</p>
		
		<p>
		<div class="form-group">
			<div class="controls">
				<button type="submit" class="btn btn-success">Sign up</button>
			</div>
		</div>
		</p>
	</fieldset>
</form>