<?php

foreach ($results->about_me->bio as $jsons) {
    echo '<p>' . doMarkdownLinks($jsons) . '</p>';
}