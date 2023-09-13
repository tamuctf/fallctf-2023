<?php
foreach(stream_get_wrappers() as &$stream) {
  stream_wrapper_unregister($stream);
}

stream_wrapper_restore('file')
?>
