<?php
include_once 'Session.php';

if(empty($_COOKIE['session']))
{
    $sess = new Session;
    $sess->username = "none";
    $sess->uid = 420;

    setcookie(
        'session',
        base64_encode(serialize($sess)),
        time()+60*60*24,
        '/'
    );
    echo nl2br(file_get_contents('index.php'));
    die();
}

if (!unserialize(base64_decode($_COOKIE['session']))) {
  echo nl2br(file_get_contents('index.php'));
  echo nl2br(file_get_contents('Session.php'));
}
?>
