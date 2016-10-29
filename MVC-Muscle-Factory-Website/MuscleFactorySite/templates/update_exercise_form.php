<h3 style="color:white">Update Exercise by ID</h3>
<form action="index.php" method="post">
	<fieldset>
		<input id='action' type='hidden' name='action' value='updateExercise' />
		<p>
			<label for="ID">Enter Exercise ID:</label> <input type="number"
				id="ID" name="ID" placeholder="Exercise ID"
			required />
		</p>
		<p>
			<label for="Exercise">Exercise Name:</label> <input type="text"
				id="Exercise" name="Exercise" placeholder="New Exercise Name"
				maxlength="25" required />
		</p>
		<p>
			<label for="Description">Description:</label> <input type="text"
				id="Description" name="Description" placeholder="New Description"
				maxlength="25" required />
		</p>
		<p>
			<label for="Type">Type</label> <input type="number"
				id="Type" name="Type" placeholder="New Type"
				min="0" max="10" required />
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