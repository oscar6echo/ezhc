

let removeJsComments = function (str) {
	let newStr = str.replace(/\/\*[\s\S]*?\*\/|([^:]|^)\/\/.*$/gm, '');
	return newStr;
};

let removeBlankLines = function (str) {
	let newStr = str.replace(/^\s*[\r\n]/gm, '');
	return newStr;
};

let removeUnecessarySpace = function (str) {
	let newStr = str.replace(/(\t| {2})+/g, ' ');
	return newStr;
};

let removeAllSpace = function (str) {
	let newStr = str.replace(/\s+/g, '');
	return newStr;
};

let removeNewLine = function (str) {
	let newStr = str.replace(/\r?\n|\r/g, '');
	return newStr;
};

let minifyFunction = function(str){
	let r = str;
	r = removeJsComments(r);
	r = removeBlankLines(r);
	r = removeUnecessarySpace(r);
	r = removeNewLine(r);
	return r;
};

var options = JSON.stringify(options);

options = JSON.parse(options, function (key, value) {

	if (value && (typeof value === 'string')) {

		let value = minifyFunction(value);
		let value2 = removeAllSpace(value);
		
		let check1 = value2.startsWith('function'),
			check2 = value2.startsWith('(function');

		if (check1) {
			let startBody = value.indexOf('{') + 1;
			let endBody = value.lastIndexOf('}');
			let startArgs = value.indexOf('(') + 1;
			let endArgs = value.indexOf(')');

			return new Function(
				value.substring(startArgs, endArgs),
				value.substring(startBody, endBody)
			);
		}
		if (check2) {
			return eval(value);
		}


	}

	return value;
});
