## Installation

### Git installation

Clone the repository in your Sublime Text "Packages" directory:

    git clone https://github.com/b3n01t/sublime-jsonToPhpArray.git "json2phparray"

The "Packages" directory is located at:

* OS X:

        ~/Library/Application Support/Sublime Text 3/Packages/

* Linux:

        ~/.config/sublime-text-3/Packages/

* Windows:

        %APPDATA%/Sublime Text 3/Packages/

## Usage

1. Select the json you want to convert into a php array
2. Open the command palette
3. Select "Json object to PHP array" and hit enter.

If your selection starts with ```var x = ...```, the generated php array will be pasted in a new tab named ```x_array.php``` surrounded by the php opening and closing tags. If you run the command on a selection starting with ```var x = ...``` again, the new php array will be inserted at the begining of the already created tab called ```x_array.php```.

If your selection starts with ```{```, the generated php array will be pasted in a new tab named ```PHP_Array_array.php``` 

##Example

converts :
```javascript
var a = {
	'b': 'c'
};
```
into:

```php
<?php
/*---- PHP Array ----*/
$a = array(
	'b' => 'c'
);

?>
```

converts :
```javascript
var proj = {
	$project: {
		_id: 1,
		ta: {
			$cond: [{
					$eq: ["$_id", "focusout"]
				}, {
					$subtract: [0, '$taa']
				},
				'$taa'
			]
		}
	}
};
```
into:

```php
<?php
/*---- PHP Array ----*/
$proj = array(
	'$project'=>array(
		'_id'=> 1,
		'ta'=>array(
			'$cond'=> array(array(
					'$eq'=> array('$_id', 'focusout')
				),array(
					'$subtract'=> array(0, '$taa')
				),
				'$taa'
			)
		)
	)
);

?>
```