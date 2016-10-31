<?php
$json = file_get_contents('../pages/content.json');

$results = json_decode($json);

function doMarkdownLinks($s) {
    return preg_replace_callback('/\[(.*?)\]\((.*?)\)/', function ($matches) {
        return '<a href="' . $matches[2] . '">' . $matches[1] . '</a>';
    }, htmlspecialchars($s));
}

if( isset($_SERVER['HTTPS'] ) ) {
    $cdn = 'https://gollahalli-lh0kueshznj0hpg0fqay.netdna-ssl.com';
}else{
    $cdn = 'http://cdn.gollahalli.me';
}

$photo = 'http://res.cloudinary.com/gollahalli/image/upload/c_lfill,g_auto,h_100,q_auto:best,w_100/v1477524340/akshay_b8wb1x.jpg';

require 'blog_rss.php';
require 'about_me.php';
