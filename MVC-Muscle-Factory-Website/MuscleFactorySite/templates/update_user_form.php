<form action="index.php" method="post">
	<fieldset>
		<input id='action' type='hidden' name='action' value='updateUser' />
		<p>
			<label for="Password">New Password:</label> <input type="password"
				id="Password" name="Password" placeholder="password"
				maxlength="25" required />
		</p>
		<p>
			<label for="Email"> New Email:</label> <input type="email"
				id="Email" name="Email" placeholder="email"
				maxlength="50" required />
		</p>
		
		<p>
		<div class="form-group">
			<div class="controls">
				<button type="submit" class="btn btn-success">Update</button>
			</div>
		</div>
		</p>
	</fieldset>
</form>