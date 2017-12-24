
options = JSON.stringify(options);

options = JSON.parse(options, function (key, value) {

	if (value && (typeof value === "string")) {

		// replace spaces then newline characters
		var check1 = (value.replace(/\s+/g, '').replace(/\r?\n|\r/g, '').substr(0, 8) == "function"),
			check2 = (value.replace(/\s+/g, '').replace(/\r?\n|\r/g, '').substr(0, 9) == "(function");


		if (check1) {
			var startBody = value.indexOf('{') + 1;
			var endBody = value.lastIndexOf('}');
			var startArgs = value.indexOf('(') + 1;
			var endArgs = value.indexOf(')');

			return new Function(value.substring(startArgs, endArgs),
				value.substring(startBody, endBody));
		}
		if (check2) {
			return eval(value);
		}

	}

	return value;

});