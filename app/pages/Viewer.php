<?php


namespace Gollahalli;


class Viewer
{
    function file_reader(){
        $json = file_get_contents('content.json');

        $results = json_decode($json);

        return $results;
    }

}