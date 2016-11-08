<?php

function tutorials()
{
    global $results, $cdn;
    $ret = '';

    foreach ($results->tutorials as $jsons) {
        $ret .= '<div class="col-lg-1">';
        $ret .= '<a href="#' . $jsons->title . '_model" data-toggle="modal" data-target="#' . $jsons->title . '_model" class="portfolio-box">';
        $ret .= '<img src="'. $cdn .'/assets/img/portfolio/tut/' . $jsons->title . '.jpg" class="img-responsive" alt="' . $jsons->title . '">';
        $ret .= '<div class="portfolio-box-caption"><div class="portfolio-box-caption-content">';
        $ret .= '<div class="project-name">' . $jsons->title . '</div>';
        $ret .= '<i class="fa fa-clone port"></i></div>';
        $ret .= '</div></a></div>';
    }
    return $ret;
}

function tutorials_models()
{
    global $results;
    $ret = '';

    foreach ($results->tutorials as $jsons) {
        $ret .= '<div class="modal fade" id="'. $jsons->title .'_model" tabindex="-1" role="dialog" aria-labelledby="'. $jsons->title .'_model_label">';
        $ret .= '<div class="modal-dialog" role="document"><div class="modal-content"><div class="modal-header">';
        $ret .= '<button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>';
        $ret .= '<h4 class="modal-title" id="jcal_model_label">'. $jsons->title .'</h4></div>';
        $ret .= '<div class="modal-body"><p>'. doMarkdownLinks($jsons->long_description) .'</p></div></div></div></div>';

    }
    return $ret;
}