<?php

// access URL and request method
$url = 'https://api.idxbroker.com/leads/property/1';
$data = array(
	'propertyName'=>'ruins',
	'property'=>array('idxID'=>'a001','listingID'=>345678)
);
$data = http_build_query($data); // encode and & delineate
$method = 'PUT';

// headers (required and optional)
$headers = array(
	'Content-Type: application/x-www-form-urlencoded', // required
	'accesskey: NDd@2a7om0nIoZdFKqjXxX', // required - replace with your own
	'outputtype: json' // optional - overrides the preferences in our API control page
);

// set up cURL
$handle = curl_init();
curl_setopt($handle, CURLOPT_URL, $url);
curl_setopt($handle, CURLOPT_HTTPHEADER, $headers);
curl_setopt($handle, CURLOPT_RETURNTRANSFER, true);
curl_setopt($handle, CURLOPT_SSL_VERIFYHOST, false);
curl_setopt($handle, CURLOPT_SSL_VERIFYPEER, false);

if ($method != 'GET')
	curl_setopt($handle, CURLOPT_CUSTOMREQUEST, $method);
// send the data
curl_setopt($handle, CURLOPT_POSTFIELDS, $data);

// exec the cURL request and returned information. Store the returned HTTP code in $code for later reference
$response = curl_exec($handle);
$code = curl_getinfo($handle, CURLINFO_HTTP_CODE);

if ($code >= 200 || $code < 300)
	$response = json_decode($response,true);
else
	$error = $code;

  var_dump($response);





 ?>
