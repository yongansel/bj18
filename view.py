import concurrent.futures


def stage1(input_data):
    # Stage 1 processing
    output_data = input_data * 2
    return output_data


def stage2(input_data):
    # Stage 2 processing
    output_data = input_data + 5
    return output_data


def main_pipeline(input_data):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Start stage 1 processing
        future1 = executor.submit(stage1, input_data)
        # Start stage 2 processing
        future2 = executor.submit(stage2, input_data)

        # Get results from both stages
        result1 = future1.result()
        result2 = future2.result()

        # Final processing with results from both stages
        final_result = result1 + result2
        return final_result


if __name__ == "__main__":
    input_data = 10
    final_output = main_pipeline(input_data)
    print("Final output:", final_output)
