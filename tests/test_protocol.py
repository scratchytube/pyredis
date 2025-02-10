#if an incomplete simple string is received the parser should not return a valid frame and not consume any bytes from the buffer
def test_read_frame_simple_string_incomplete_frame():
  # checks to see if message is complete based on if \r\n is present
  buffer = b"+PartialData"
  frame, frame_size = extract_frame_from_buffer(buffer)
  # checks to see buffer is not a valid complete message
  assert frame == None
  # checks to see that zero bytes were processed
  assert frame_size == 0