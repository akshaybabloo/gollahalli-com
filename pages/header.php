<?php
$json = file_get_contents('pages/content.json');

$results = json_decode($json);

function doMarkdownLinks($s) {
    return preg_replace_callback('/\[(.*?)\]\((.*?)\)/', function ($matches) {
        return '<a href="' . $matches[2] . '">' . $matches[1] . '</a>';
    }, htmlspecialchars($s));
}

require 'about_me.php';
require 'publication.php';
require 'experience.php';
require 'skills.php';
require 'blog_rss.php';
require 'projects.php';
require 'tutorials.php';