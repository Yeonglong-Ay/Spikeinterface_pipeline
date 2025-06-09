import spikeinterface.sorters as ss
import spikeinterface.extractors as se


test_recording, _ = se.toy_example(
    duration=30,
    seed=0,
    num_channels=64,
    num_segments=1
)
test_recording = test_recording.save(folder="test-docker-folder", overwrite=True)

sorting = ss.run_sorter(sorter_name='kilosort3',
    recording=test_recording,
    output_folder="kilosort3",
    singularity_image=True)

print(sorting)
