<?php
include 'bulletproof.php';

session_start();
$sess = basename(session_id());

if($sess !== session_id()) {
  echo "ERROR: Invalid session cookie. Please delete the PHPSESSID cookie.";
  die();
}

if(!file_exists('/tmp/uploads/' . $sess)) {
  mkdir('/tmp/uploads/' . $sess, 0755, true);
}

if($_SERVER['REQUEST_METHOD'] === 'POST') {
  $image = new Bulletproof\Image($_FILES);
  if($image['toUpload']) {
    $image->setLocation("/tmp/uploads/" . $sess);
    $image->setSize(100, 3000000);
    $image->setMime(array('jpeg', 'gif', 'png'));
    $upload = $image->upload();

    if($upload) {
      header('Location: /index.php?message=Image uploaded successfully&status=success');
    } else {
      header('Location: /index.php?message=Image upload failed&status=fail');
    }
  } else {
    header('Location: /index.php?message=Image upload failed&status=fail');
  }
}
?>

<!DOCTYPE html>
<html>
<head>
<title>Family Image Storage</title>
<link href='static/style.css' rel='stylesheet'>
</head>
<body>
<div class=header>
  <div class=title-image>
    <img src="static/logo.png">
  </div>
  <div class=title>
    <h1>Family Image Storage</h1>
  </div>
</div>
<div class=page>
  <div class=content>
    <form class="image-upload-form" enctype="multipart/form-data" method="POST" action="/">
      <div class="file-select">
        <div class="upload-bar">
          <div class="file-select-btn" id="fileName">Choose File</div>
          <div class="file-select-name" id="noFile">No file chosen...</div>
          <input type="file" accept="image/png,image/jpeg,image/gif" name="toUpload" id="chooseFile" required>
        </div>
        <div class="submit">
          <p>Upload</p>
          <input type="submit" value="Submit">
        </div>
      </div>
      <div class="result" id="result">
      </div>
    </form>
    <div class=image-display>
<?php
if(scandir('/tmp/uploads/' . $sess) != False) {
  $files = array_diff(scandir('/tmp/uploads/' . $sess), array('.', '..'));

  foreach($files as &$f) {
    echo "<a href=/download/" . $sess . "/" . $f . "><div class=card><img class=thumbnail src=/download/" . $sess . "/" . $f . "></div></a>";
  }
}
?>
    </div>
  </div>
</div>
  <script src="static/jquery/jquery.min.js"></script>
  <script>
    (function ($) {
      $('#chooseFile').bind('change', function() {
        var filename = $('#chooseFile').val();
        if(/^\s*$/.test(filename)) {
          $('.upload-bar').removeClass('active');
          $('#noFile').text("No file chosen...");
        } else {
          $('.upload-bar').addClass('active');
          $('#noFile').text(filename.replace("C:\\fakepath\\", ""));
        }
      });
    })(window.jQuery);
  </script>
  <script>
    const params = new URLSearchParams(window.location.search);
    if(params.has('message') && params.has('status')) {
      if(params.get('status') == 'success') {
        document.getElementById("result").style.color = '#3fa46a';
        document.getElementById("result").innerText = params.get('message');
      } else {
        document.getElementById("result").style.color = '#dc3545';
        document.getElementById("result").innerText = params.get('message');
      }
    }
  </script>
</body>
</html>
