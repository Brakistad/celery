# TrackIdent Process
### notes from meeting
#### Download cdc data for one week
#### Geofencing each station. (used for downloaded segments)
#### Split files into station segments
#### Cleaning process (different process for elev.diag and no elev)
##### Remove timestamp =>(relative seconds since start)
##### Sort into two groups inbound, outbound
#### Fetch track model from elevation diagram (elev.diag)
#### “Combine” gps and track model estimates. (elev.diag)
#### Sum up ax to estimate position. (m along the track) (elev.diag)
#### Calculate sonogram.