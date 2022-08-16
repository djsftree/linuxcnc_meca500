### linuxcnc_meca500

1). install meca500gui to /local/usr/bin  (generates debian package)

```
sudo scripts/install.sh
```

2). run axis sim
```
linuxcnc linuxcnc/configs/sim-meca500/sim-meca500.ini
```

3). manipulate a meca500 vtk demo app
```
cd share/models
python3 meca500.py
```

4). current sim DH here
https://github.com/djsftree/linuxcnc_meca500/blob/main/linuxcnc/configs/sim-meca500/meca500-kinematics.hal
