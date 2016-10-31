<?php
$json = file_get_contents('pages/content.json');

$results = json_decode($json);

function doMarkdownLinks($s) {
    return preg_replace_callback('/\[(.*?)\]\((.*?)\)/', function ($matches) {
        return '<a href="' . $matches[2] . '">' . $matches[1] . '</a>';
    }, htmlspecialchars($s));
}

function addScheme($url, $scheme = 'https://')
{
    return parse_url($url, PHP_URL_SCHEME) === null ?
        $scheme . $url : $url;
}

if( isset($_SERVER['HTTPS'] ) ) {
    $cdn = 'https://gollahalli-lh0kueshznj0hpg0fqay.netdna-ssl.com';
}else{
    $cdn = 'http://cdn.gollahalli.me';
}

$photo = 'http://res.cloudinary.com/gollahalli/image/upload/c_lfill,g_auto,h_200,q_auto:best,w_200/v1477524340/akshay_b8wb1x.jpg';

require 'about_me.php';
require 'publication.php';
require 'experience.php';
require 'skills.php';
require 'blog_rss.php';
require 'projects.php';
require 'tutorials.php';