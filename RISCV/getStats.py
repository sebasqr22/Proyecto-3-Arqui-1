import os
import re

def parse_stats_file(filename):
    stats = {}
    with open(filename, 'r') as f:
        for line in f:
            match = re.match(r"(\S+)\s+(\d+\.?\d*)", line)
            if match:
                stats[match.group(1)] = float(match.group(2))
    return stats

def extract_relevant_stats(stats):
    relevant_stats = {}

    # Cache misses and accesses
    relevant_stats['L1D Cache Misses'] = stats.get('system.cpu.dcache.overallMisses::total', 0)
    relevant_stats['L1I Cache Misses'] = stats.get('system.cpu.icache.overallMisses::total', 0)
    relevant_stats['L1D Cache Accesses'] = stats.get('system.cpu.dcache.overallAccesses::total', 0)
    relevant_stats['L1I Cache Accesses'] = stats.get('system.cpu.icache.overallAccesses::total', 0)
    
    # Cache miss rates
    relevant_stats['L1D Cache Miss Rate'] = (relevant_stats['L1D Cache Misses'] / relevant_stats['L1D Cache Accesses']) if relevant_stats['L1D Cache Accesses'] > 0 else 0
    relevant_stats['L1I Cache Miss Rate'] = (relevant_stats['L1I Cache Misses'] / relevant_stats['L1I Cache Accesses']) if relevant_stats['L1I Cache Accesses'] > 0 else 0

    # Branch predictor stats
    relevant_stats['Branch Predictor Lookups'] = stats.get('system.cpu.branchPred.lookups', 0)
    relevant_stats['Conditional Branches Predicted'] = stats.get('system.cpu.branchPred.condPredicted', 0)
    relevant_stats['Conditional Branches Incorrect'] = stats.get('system.cpu.branchPred.condIncorrect', 0)
    relevant_stats['Indirect Misses'] = stats.get('system.cpu.branchPred.indirectMisses', 0)
    relevant_stats['Indirect Mispredicted'] = stats.get('system.cpu.branchPred.indirectMispredicted', 0)

    return relevant_stats

def write_relevant_stats_to_file(relevant_stats, output_filename):
    with open(output_filename, 'w') as f:
        for key, value in relevant_stats.items():
            f.write(f"{key}: {value}\n")

# Main function
def main():
    input_directory = 'stats_files'
    output_directory = 'relevant_stats'

    # Create output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Process each stats file
    for filename in os.listdir(input_directory):
        if filename.endswith(".txt"):
            input_filename = os.path.join(input_directory, filename)
            output_filename = os.path.join(output_directory, f"{os.path.splitext(filename)[0]}_relevant.txt")

            stats = parse_stats_file(input_filename)
            relevant_stats = extract_relevant_stats(stats)
            write_relevant_stats_to_file(relevant_stats, output_filename)
            print(f"Relevant stats extracted and saved to {output_filename}")

if __name__ == "__main__":
    main()
