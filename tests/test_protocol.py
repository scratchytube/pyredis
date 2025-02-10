def test_read_frame_simple_string_incomplete_frame():
  # checks to see if message is complete based on if \r\n is present
  buffer = b"+PartialData"
  # checks to see buffer is not a valid complete message
  assert frame == None
  # checks to see that zero bytes were processed
  assert frame_size == 0