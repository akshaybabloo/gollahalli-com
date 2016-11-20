<?php

function get_repo()
{
    // A token that you could generate from your own github
    // go here https://github.com/settings/applications and create a token
    // then replace the next string
    $token = '8dc33695f58ca9513736c37126871ab6376e7c0e';

    // We generate the url for curl
    $curl_url = 'https://api.github.com/repos/akshaybabloo/gollahalli-me/releases/latest';

    // We generate the header part for the token
    $curl_token_auth = 'Authorization: token ' . $token;

    // We make the actuall curl initialization
    $ch = curl_init($curl_url);

    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);

    // We set the right headers: any user agent type, and then the custom token header part that we generated
    curl_setopt($ch, CURLOPT_HTTPHEADER, array('User-Agent: Chrome', $curl_token_auth));

    // We execute the curl
    $output = curl_exec($ch);

    // And we make sure we close the curl
    curl_close($ch);

    // Then we decode the output and we could do whatever we want with it
    $output = json_decode($output);
    //highlight_string("<?php\n\$data =\n" . var_export($output, true) . ";\n

    return $output;

}