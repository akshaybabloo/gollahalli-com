<?php
$json = file_get_contents('../content.json');

$results = json_decode($json);

function doMarkdownLinks($s) {
    return preg_replace_callback('/\[(.*?)\]\((.*?)\)/', function ($matches) {
        return '<a href="' . $matches[2] . '">' . $matches[1] . '</a>';
    }, htmlspecialchars($s));
}

function addScheme($url, $scheme = 'https:')
{
    return preg_replace("/^http:/i", $scheme, $url);
}

$cdn = 'https://cdn.gollahalli.me';

$photo = 'https://res.cloudinary.com/gollahalli/image/upload/c_lfill,g_auto,h_100,q_auto:best,w_100/v1477524340/akshay_b8wb1x.jpg';

require 'blog_rss.php';
require 'about_me.php';
require 'publication.php';
require 'skills.php';
require 'experience.php';
require 'projects.php';
require 'tutorials.php';

require_once ('../../vendor/autoload.php');