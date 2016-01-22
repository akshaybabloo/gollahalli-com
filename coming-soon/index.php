<?php
    if (!isset($_SERVER['HTTPS']) || $_SERVER['HTTPS'] !== 'on') {
        if(!headers_sent()) {
            header("Status: 301 Moved Permanently");
            header(sprintf(
                'Location: https://%s%s',
                $_SERVER['HTTP_HOST'],
                $_SERVER['REQUEST_URI']
            ));
            exit();
        }
    }
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <base href="https://www.gollahalli.me">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="Akshay Raj Gollahalli is a PhD student in AUT university and this website showcases his work.">
    <meta name="author" content="Akshay Raj Gollahalli">
    <meta name="keywords" content="computer science, brain computer interface, artificial intelligence"/>
    <meta name="rights" content="All rights reserved by Akshay Raj Gollahalli" />
    <link rel="icon" href="img/favicon.ico">

    <title>Akshay Raj Gollahalli - Home</title>

    <!-- Bootstrap core CSS -->
    <link href="css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="css/cover.css" rel="stylesheet">

    <link rel="stylesheet" href="font-awesome/css/font-awesome.min.css" type="text/css">

    <script>
        (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
                (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
            m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
        })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

        ga('create', 'UA-72583688-1', 'auto');
        ga('send', 'pageview');

    </script>

    <script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0],p=/^http:/.test(d.location)?'http':'https';if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src=p+"://platform.twitter.com/widgets.js";fjs.parentNode.insertBefore(js,fjs);}}(document,"script","twitter-wjs");</script>


    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
    <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
    <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->
</head>

<body>

<div class="site-wrapper">

    <div class="site-wrapper-inner">

        <div class="cover-container">

            <div class="inner cover">
                <h1 class="cover-heading">gollahalli</h1>
                <p class="lead">Coming soon!</p>
                <p class="lead">
                    <a href="https://www.facebook.com/akshaybabloo"><i class="fa fa-facebook"></i></a>
                    <a href="https://twitter.com/akshaybabloo"><i class="fa fa-twitter"></i></a>
                    <a href="https://nz.linkedin.com/in/gollahalli"><i class="fa fa-linkedin"></i></a>
                </p>
                <p class="lead">
                    <a class="twitter-timeline" href="https://twitter.com/akshaybabloo" width="300" height="300" data-widget-id="690023186424012800">Tweets by @akshaybabloo</a>
                </p>
            </div>

        </div>

    </div>

</div>


<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
<script>window.jQuery || document.write('<script src="js/jquery.js"><\/script>')</script>
<script src="js/bootstrap.min.js"></script>
</body>
</html>
