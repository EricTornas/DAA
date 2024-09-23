import os
import subprocess

def run_test(test_input, expected_output,code):
    # Corre la solución usando el test_input y captura la salida
    current_directory = os.path.dirname(os.path.abspath(__file__))
    code = current_directory + '\\'+code+'.py'
    actual_output  = subprocess.run(
    ['python', '-u', code],
    input=test_input,
    text=True,
    capture_output=True
    )
    return int(actual_output.stdout) == int(expected_output), actual_output.stdout

def run_all_tests():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    test_cases_dir = current_directory +'\\test_cases.txt'
    expected_outputs_dir = current_directory +'\\expected_outputs.txt'

        
    with open(test_cases_dir, 'r') as test_input_file:
        test_input = test_input_file.read()
    
    with open(expected_outputs_dir, 'r') as expected_output_file:
        expected_output = expected_output_file.read()
        
        passed_dp, actual_output_dp = run_test(test_input, expected_output, 'dp')
        passed_fb, actual_output_fb = run_test(test_input, expected_output, 'backtrack')
        passed_greedy, actual_output_greedy = run_test(test_input, expected_output, 'greedy')
        
    if passed_dp:
        print(f"Test DP: PASSED")
    else:
        print(f"Test DP: FAILED")
        print(f"Expected: {expected_output}")
        print(f"Actual: {actual_output_dp}")

    if passed_fb:
        print(f"Test BACKTRACK: PASSED")
    else:
        print(f"Test BACKTRACK: FAILED")
        print(f"Expected: {expected_output}")
        print(f"Actual: {actual_output_fb}")

    if passed_greedy:
        print(f"Test GREEDY: PASSED")
    else:
        print(f"Test GREEDY: FAILED")
        print(f"Expected: {expected_output}")
        print(f"Actual: {actual_output_greedy}")

if __name__ == "__main__":
    run_all_tests()