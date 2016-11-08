<?php

function projects()
{
    global $results, $cdn;
    $ret = '';

    foreach ($results->projects as $jsons) {
        $ret .= '<div class="col-lg-4 col-sm-6">
                <a href="#' . $jsons->title . '_model" data-toggle="modal" data-target="#' . $jsons->title . '_model" class="portfolio-box">
                <img src="'. $cdn .'/img/portfolio/' . $jsons->title . '.jpg" class="img-responsive" alt="' . $jsons->title . '">';
        $ret .= '<div class="portfolio-box-caption">
                        <div class="portfolio-box-caption-content">
                            <div class="project-category text-faded">
                            ' . $jsons->category . '
                            </div>';
        $ret .= '<div class="project-name">
                                ' . $jsons->title . '
                            </div>';
        $ret .= '<p><i class="text-faded">' . $jsons->short_description . '</i></p>
                            <i class="fa fa-clone port"></i>
                        </div>';
        $ret .= '</div>
                </a>
            </div>';
    }
    return $ret;
}

function projects_models()
{
    global $results;
    $ret = '';

    foreach ($results->projects as $jsons) {
        $ret .= '<div class="modal fade" id="'. $jsons->title .'_model" tabindex="-1" role="dialog" aria-labelledby="'. $jsons->title .'_model_label">';
        $ret .= '<div class="modal-dialog" role="document">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span
                        aria-hidden="true">&times;</span></button>
                <h4 class="modal-title" id="jcal_model_label">'. $jsons->title .'</h4></div>';
        $ret .= '<div class="modal-body">
                <p>'. doMarkdownLinks($jsons->long_description) .'</p></div></div>
    </div>
</div>';

    }
    return $ret;
}