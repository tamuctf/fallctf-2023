<?php
class Session {
  public $username;
  public $uid;

  public function __destruct() {
    if($this->username === "admin" && $this->uid === 0) {
      echo file_get_contents('../flag.txt');
      return True;
    }
    return False;
  }
}
?>
