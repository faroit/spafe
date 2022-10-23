from scipy.io.wavfile import read
from spafe.features.psrcc import psrcc
from spafe.utils.vis import show_features

# read audio
fpath = "../../../test.wav"
fs, sig = read(fpath)

# compute psrccs
psrccs  = psrcc(sig,
                fs=fs,
                pre_emph=1,
                pre_emph_coeff=0.97,
                win_len=0.030,
                win_hop=0.015,
                win_type="hamming",
                nfilts=128,
                nfft=2048,
                low_freq=0,
                high_freq=8000,
                normalize="mvn")

# visualize features
show_features(psrccs, "Phase based Spectral Root Cepstral Coefficients", "PSRCC Index", "Frame Index")