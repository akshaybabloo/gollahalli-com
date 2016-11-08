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
            $ret .= '<div class="cd-timeline-block">';
            if ($j->current) {
                $ret .= '<div class="cd-timeline-img cd-picture">';
            } else {
                $ret .= '<div class="cd-timeline-img cd-movie">';
            }
            $ret .= '<img src="'. $cdn .'/assets/img/grad.png" alt="Grad-pic">
                        </div>
                        <div class="cd-timeline-content">';
            $ret .= '<h4>' . $j->title . '</h4>';

            $ret .= '<p class="text-muted">' . $j->where . '</p>';
            $ret .= '<span class="cd-date">' . $j->from . ' - ' . $j->to . '</span>';
            $ret .= '</div></div>';
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
