/* Master 0, Slave 0
 * Vendor ID:       0x00ecade1
 * Product code:    0x0004d500
 * Revision number: 0x00000001
 */

ec_pdo_entry_info_t slave_0_pdo_entries[] = {
    {0x7200, 0x01, 1}, /* Deactivate */
    {0x7200, 0x02, 1}, /* Activate */
    {0x7200, 0x03, 1}, /* Home */
    {0x7200, 0x04, 1}, /* Reset Error */
    {0x7200, 0x05, 1}, /* Sim Mode */
    {0x7200, 0x06, 1}, /* Recovery Mode */
    {0x0000, 0x00, 26}, /* Gap */
    {0x7310, 0x01, 16}, /* Move ID */
    {0x7310, 0x02, 1}, /* SetPoint */
    {0x7310, 0x03, 1}, /* Pause */
    {0x7310, 0x04, 1}, /* Clear Move */
    {0x7310, 0x05, 1}, /* Reset PStop */
    {0x0000, 0x00, 12}, /* Gap */
    {0x7305, 0x00, 32}, /* Move Command */
    {0x7306, 0x01, 32}, /* SubIndex 001 */
    {0x7306, 0x02, 32}, /* SubIndex 002 */
    {0x7306, 0x03, 32}, /* SubIndex 003 */
    {0x7306, 0x04, 32}, /* SubIndex 004 */
    {0x7306, 0x05, 32}, /* SubIndex 005 */
    {0x7306, 0x06, 32}, /* SubIndex 006 */
    {0x7400, 0x00, 32}, /* Host Time */
    {0x7410, 0x01, 1}, /* BrakesControlAllowed */
    {0x7410, 0x02, 1}, /* BrakesEngaged */
    {0x0000, 0x00, 30}, /* Gap */
    {0x7420, 0x00, 32}, /* SubIndex 000 */
    {0x7421, 0x00, 32}, /* SubIndex 000 */
    {0x7422, 0x00, 32}, /* SubIndex 000 */
    {0x7423, 0x00, 32}, /* SubIndex 000 */
    {0x6010, 0x02, 1}, /* Busy */
    {0x6010, 0x03, 1}, /* Activated */
    {0x6010, 0x04, 1}, /* Homed */
    {0x6010, 0x05, 1}, /* SimActivated */
    {0x6010, 0x06, 1}, /* BrakesEngaged */
    {0x6010, 0x07, 1}, /* RecoveryMode */
    {0x0000, 0x00, 10}, /* Gap */
    {0x6010, 0x01, 16}, /* Error */
    {0x6015, 0x01, 32}, /* CheckPoint */
    {0x6015, 0x02, 16}, /* Move ID */
    {0x6015, 0x03, 16}, /* FIFO Space */
    {0x6015, 0x05, 1}, /* Paused */
    {0x6015, 0x06, 1}, /* EOB */
    {0x6015, 0x07, 1}, /* EOM */
    {0x6015, 0x08, 1}, /* FIFO Cleared */
    {0x6015, 0x09, 1}, /* PStop */
    {0x6015, 0x0a, 1}, /* Excessive torque */
    {0x0000, 0x00, 10}, /* Gap */
    {0x6015, 0x04, 16}, /* Offline Program ID */
    {0x6030, 0x01, 32}, /* SubIndex 001 */
    {0x6030, 0x02, 32}, /* SubIndex 002 */
    {0x6030, 0x03, 32}, /* SubIndex 003 */
    {0x6030, 0x04, 32}, /* SubIndex 004 */
    {0x6030, 0x05, 32}, /* SubIndex 005 */
    {0x6030, 0x06, 32}, /* SubIndex 006 */
    {0x6031, 0x01, 32}, /* SubIndex 001 */
    {0x6031, 0x02, 32}, /* SubIndex 002 */
    {0x6031, 0x03, 32}, /* SubIndex 003 */
    {0x6031, 0x04, 32}, /* SubIndex 004 */
    {0x6031, 0x05, 32}, /* SubIndex 005 */
    {0x6031, 0x06, 32}, /* SubIndex 006 */
    {0x6046, 0x01, 8}, /* Shoulder */
    {0x6046, 0x02, 8}, /* Elbow */
    {0x6046, 0x03, 8}, /* Wrist */
    {0x6046, 0x04, 8}, /* Turn */
    {0x6050, 0x01, 32}, /* SubIndex 001 */
    {0x6050, 0x02, 32}, /* SubIndex 002 */
    {0x6050, 0x03, 32}, /* SubIndex 003 */
    {0x6050, 0x04, 32}, /* SubIndex 004 */
    {0x6050, 0x05, 32}, /* SubIndex 005 */
    {0x6050, 0x06, 32}, /* SubIndex 006 */
    {0x6051, 0x01, 32}, /* SubIndex 001 */
    {0x6051, 0x02, 32}, /* SubIndex 002 */
    {0x6051, 0x03, 32}, /* SubIndex 003 */
    {0x6051, 0x04, 32}, /* SubIndex 004 */
    {0x6051, 0x05, 32}, /* SubIndex 005 */
    {0x6051, 0x06, 32}, /* SubIndex 006 */
    {0x6060, 0x01, 32}, /* Timestamp Seconds */
    {0x6060, 0x02, 32}, /* Timestamp Microseconds */
    {0x6060, 0x03, 32}, /* Dynamic Data Cycles */
    {0x0000, 0x00, 32}, /* Gap */
    {0x0000, 0x00, 32}, /* Gap */
    {0x0000, 0x00, 32}, /* Gap */
    {0x6070, 0x01, 32}, /* Dynamic Type */
    {0x6070, 0x02, 32}, /* Value 0 */
    {0x6070, 0x03, 32}, /* Value 1 */
    {0x6070, 0x04, 32}, /* Value 2 */
    {0x6070, 0x05, 32}, /* Value 3 */
    {0x6070, 0x06, 32}, /* Value 4 */
    {0x6070, 0x07, 32}, /* Value 5 */
    {0x6071, 0x01, 32}, /* Dynamic Type */
    {0x6071, 0x02, 32}, /* Value 0 */
    {0x6071, 0x03, 32}, /* Value 1 */
    {0x6071, 0x04, 32}, /* Value 2 */
    {0x6071, 0x05, 32}, /* Value 3 */
    {0x6071, 0x06, 32}, /* Value 4 */
    {0x6071, 0x07, 32}, /* Value 5 */
    {0x6072, 0x01, 32}, /* Dynamic Type */
    {0x6072, 0x02, 32}, /* Value 0 */
    {0x6072, 0x03, 32}, /* Value 1 */
    {0x6072, 0x04, 32}, /* Value 2 */
    {0x6072, 0x05, 32}, /* Value 3 */
    {0x6072, 0x06, 32}, /* Value 4 */
    {0x6072, 0x07, 32}, /* Value 5 */
    {0x6073, 0x01, 32}, /* Dynamic Type */
    {0x6073, 0x02, 32}, /* Value 0 */
    {0x6073, 0x03, 32}, /* Value 1 */
    {0x6073, 0x04, 32}, /* Value 2 */
    {0x6073, 0x05, 32}, /* Value 3 */
    {0x6073, 0x06, 32}, /* Value 4 */
    {0x6073, 0x07, 32}, /* Value 5 */
};

ec_pdo_info_t slave_0_pdos[] = {
    {0x1600, 7, slave_0_pdo_entries + 0}, /* Robot Control */
    {0x1601, 6, slave_0_pdo_entries + 7}, /* Motion Control */
    {0x1602, 7, slave_0_pdo_entries + 13}, /* Move */
    {0x1610, 1, slave_0_pdo_entries + 20}, /* Host Time */
    {0x1611, 3, slave_0_pdo_entries + 21}, /* Brakes Control */
    {0x1620, 1, slave_0_pdo_entries + 24}, /* Dynamic Data Cfg 0 */
    {0x1621, 1, slave_0_pdo_entries + 25}, /* Dynamic Data Cfg 1 */
    {0x1622, 1, slave_0_pdo_entries + 26}, /* Dynamic Data Cfg 2 */
    {0x1623, 1, slave_0_pdo_entries + 27}, /* Dynamic Data Cfg 3 */
    {0x1a00, 8, slave_0_pdo_entries + 28}, /* Robot Status */
    {0x1a01, 11, slave_0_pdo_entries + 36}, /* Motion Status */
    {0x1a02, 6, slave_0_pdo_entries + 47}, /* Joint Set */
    {0x1a03, 6, slave_0_pdo_entries + 53}, /* End-Effector Pose */
    {0x1a08, 4, slave_0_pdo_entries + 59}, /* Configurations */
    {0x1a09, 6, slave_0_pdo_entries + 63}, /* WRF */
    {0x1a0a, 6, slave_0_pdo_entries + 69}, /* TRF */
    {0x1a10, 6, slave_0_pdo_entries + 75}, /* Robot Timestamp */
    {0x1a20, 7, slave_0_pdo_entries + 81}, /* Dynamic Data 0 */
    {0x1a21, 7, slave_0_pdo_entries + 88}, /* Dynamic Data 1 */
    {0x1a22, 7, slave_0_pdo_entries + 95}, /* Dynamic Data 2 */
    {0x1a23, 7, slave_0_pdo_entries + 102}, /* Dynamic Data 3 */
};

ec_sync_info_t slave_0_syncs[] = {
    {0, EC_DIR_OUTPUT, 0, NULL, EC_WD_DISABLE},
    {1, EC_DIR_INPUT, 0, NULL, EC_WD_DISABLE},
    {2, EC_DIR_OUTPUT, 9, slave_0_pdos + 0, EC_WD_ENABLE},
    {3, EC_DIR_INPUT, 12, slave_0_pdos + 9, EC_WD_DISABLE},
    {0xff}
};

