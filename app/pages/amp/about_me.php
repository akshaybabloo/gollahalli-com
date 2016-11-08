<?php
function about_me_bio()
{
    $ret = '';
    global $results;
    foreach ($results->about_me->bio as $jsons) {
        $ret .= '<p>' . doMarkdownLinks($jsons) . '</p>';
    }
    return $ret;
}

function about_me_education()
{
    global $results, $cdn;
    $ar = array();
    $ret = '';
    foreach ($results->about_me->education as $jsons) {
        array_push($ar, $jsons);
    }

    foreach (array_reverse($ar) as $j) {
        $ret .= '<div class="time-line-item">';
        $ret .= '<amp-img ';
        if ($j->current) {
            $ret .= 'class="yes-true"';
        } else {
            $ret .= 'class="no-false"';
        }
        $ret .= ' src="'. $cdn .'/img/grad.png"
                width="30"
                height="30"
                layout="fixed"
                attribution="Grad-pi"
                on="tap:timeline_lightbox_1"
                role="button"
                tabindex="0"></amp-img>';

        $ret .= '<h4 class="margin-0">' . $j->title . '<small>'. ' ' . $j->from . '-'. $j->to .'</small></h4>';
        $ret .= '<p class="margin-0">' . $j->where . '</p>';
        $ret .= '</div>';
    }
    return $ret;
}

function about_me_research_area()
{
    global $results;
    $ret = '';
    $ret .= '<ul>';
    foreach ($results->research_area as $jsons) {
        $ret .= '<li>' . $jsons . '</li>';
    }
    $ret .= '</ul>';
    return $ret;
}